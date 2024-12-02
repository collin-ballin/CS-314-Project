# ChocAn System

## Database Setup
1. Create PostgreSQL database:
CREATE DATABASE choco;


2. Create user:
CREATE USER dev WITH PASSWORD 'guest';

3. Load Schema:
psql -U dev -d choco -f database/schema/database_schema.sql

## Install Libraries:
psycopg2

## Install Database:
postgress
