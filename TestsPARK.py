from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

if __name__ == "__main__":
    spark = SparkSession.builder.master("local[*]").appName("yajvendra").getOrCreate()
    spark.createDataFrame([(1, "value1"), (2, "value2")], ["id", "value"]).show()

    # data2 = [
    #     ("James", "", "Smith", "36636", "M", 3000),
    #     ("Michael", "Rose", "", "40288", "M", 4000),
    #     ("Robert", "", "Williams", "42114", "M", 4000),
    #     ("Maria", "Anne", "Jones", "39192", "F", 4000),
    #     ("Jen", "Mary", "Brown", "", "F", -1)
    # ]
    # schema = StructType(
    #     [
    #         StructField("firstname", StringType(), True),
    #         StructField("middlename", StringType(), True),
    #         StructField("lastname", StringType(), True),
    #         StructField("id", StringType(), True),
    #         StructField("gender", StringType(), True),
    #         StructField("Salary", IntegerType(), True)
    #     ]
    # )
    # sparkContext = spark.sparkContext
    # app_id = spark.sparkContext.getConf().get('spark.app.id')
    # app_name = spark.sparkContext.getConf().get('spark.app.name')
    # message_prefix = '<' + app_name + ' ' + app_id + '>'
    # # self.logger = log4j.LogManager.getLogger(message_prefix)
    # print(message_prefix)
    #
    # spark.createDataFrame(data=data2, schema=schema).show()

    ds1 = spark.range(1, 10000000)
    ds2 = spark.range(1, 10000000, 2)
    ds3 = ds1.repartition(7)
    ds4 = ds2.repartition(9)
    ds5 = ds3.selectExpr("id * 5 as id")
    joined = ds5.join(ds4, "id")
    sum = joined.selectExpr("sum(id)")
    print(sum.explain)

    val = input("Enter to exit : ")

