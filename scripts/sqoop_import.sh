#!/bin/bash

sqoop import \
  --connect jdbc:mysql://your-mysql-host:3306/your_db \
  --username your_user \
  --password your_password \
  --table your_table \
  --target-dir /data/raw/your_table \
  --m 1
