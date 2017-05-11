from pyspark import SparkContext
import itertools

sc = SparkContext("spark://spark-master:7077", "PopularItems")

def newtups(line):
    for tup in line[1]:
        newtup = (tup, line[0])
        yield newtup

data = sc.textFile("/app/access.log", 2)     # each worker loads a piece of the data file

pairs = data.map(lambda line: line.split(" "))   # tell each worker to split each line of it's partition
pairs2 = pairs.map(lambda line: (line[0], line[1]))
user_clicks = pairs2.groupByKey().map(lambda thelist: (thelist[0], list(thelist[1])) )
user_click_pairs = user_clicks.map(lambda line: ( line[0], list(itertools.combinations(line[1], 2))) )
flat_pairs = user_click_pairs.flatMap(newtups)
list_users = flat_pairs.groupByKey().map(lambda thelist: (thelist[0], list(thelist[1])) )
coclick_count = list_users.map(lambda line: (line[0], len(line[1])))
filtered_result = coclick_count.filter(lambda line: line[1] > 2)

output = filtered_result.collect()
for userid, clicks in output:
    print ("click pair " + str(userid) + " clicked this many times " + str(clicks))

# count = pages.reduceByKey(lambda x,y: int(x)+int(y))        # shuffle the data so that each key is only on one worker
                                                  # and then reduce all the values by adding them together
# output = count.collect()                          # bring the data back to the master node so we can print it out
# for page_id, count in output:
#     print ("page_id %s count %d" % (page_id, count))
# print ("Popular items done")

print("the job is done")
sc.stop()

# A pseudocode map-reduce style algorithm for computing co-views is something like:
#
# 1. Read data in as pairs of (user_id, item_id clicked on by the user)
# 2. Group data into (user_id, list of item ids they clicked on)
# 3. Transform into (user_id, (item1, item2) where item1 and item2 are pairs of items the user clicked on
# 4. Transform into ((item1, item2), list of user1, user2 etc) where users are all the ones who co-clicked (item1, item2)
# 5. Transform into ((item1, item2), count of distinct users who co-clicked (item1, item2)
# 6. Filter out any results where less than 3 users co-clicked the same pair of items


# Spark supports some other useful opreations on RDDs:
#
# groupByKey() - take all rows of the form (K,V) and group them into a single row of form (K, list of different Vs)
# distinct() - filter out all duplicate rows in an RDD to produce a new RDD with distinct rows
# flatMap() - like map, but returns multiple rows for when you want produce a new RDD with multiple output rows for each input row
# filter() - remove certain rows from an RDD

# RDD's support map/reduce style operations like we've discussed in class. For example, in the sample program the line

# pairs = data.map(lambda line: line.split(" "))
# applies a map operation to the data RDD to produce a new RDD called pairs. Every row of
# text in data is transformed into a row containing a Python pair/tuple in pairs. The next line

# pages = pairs.map(lambda pair: (pair[1], 1))
# applies a map operation to each row in pairs to produce a new RDD called pages where each row
# is a pair of page id and the number 1. Finally, the line

# count = pages.reduceByKey(lambda x,y: x+y)
# does a reduce operation. This groups all the rows with the same key onto the same
# worker and then reduces all the values for those keys by summing.
