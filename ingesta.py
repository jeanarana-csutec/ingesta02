import boto3
import csv
import mysql.connector

conexion = mysql.connector.connect(
    host="172.31.29.26",
    port=8005,
    user="root",
    password="utec",
    database="bd_api_employees"
)

cursor = conexion.cursor()
cursor.execute("SELECT * FROM employees")
datos = cursor.fetchall()

with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "name", "age"])
    writer.writerows(datos)

cursor.close()
conexion.close()

ficheroUpload = "data.csv"
nombreBucket = "gcr-output-01"

s3 = boto3.client("s3")
s3.upload_file(ficheroUpload, nombreBucket, ficheroUpload)

print("Ingesta completada")
