CREATE TABLE "subscribers" (
  "id" SERIAL PRIMARY KEY,
  "full_name" varchar,
  "created_at" timestamp,
  "country_code" int,
  "phone_no" int,
  "cur_plan_id" int
);

CREATE TABLE "transactions" (
  "id" SERIAL PRIMARY KEY,
  "sub_id" int,
  "type" varchar,
  "created_at" timestamp,
  "location" varchar,
  "buy_plan_id" int
);

CREATE TABLE "Plans" (
  "id" int PRIMARY KEY,
  "cost" int,
  "validity" int,
  "data" float,
  "feature_id" int,
  "Postpaid" bool
);

CREATE TABLE "usage" (
  "id" SERIAL PRIMARY KEY,
  "sub_id" int,
  "type" varchar,
  "time" timestamp,
  "amount" int
);

CREATE TABLE "features" (
  "id" SERIAL PRIMARY KEY,
  "sms" int,
  "netflix" boolean,
  "prime" boolean,
  "hotstar" boolean
);

ALTER TABLE "features" ADD FOREIGN KEY ("id") REFERENCES "Plans" ("feature_id");

ALTER TABLE "usage" ADD FOREIGN KEY ("sub_id") REFERENCES "subscribers" ("id");

ALTER TABLE "transactions" ADD FOREIGN KEY ("sub_id") REFERENCES "subscribers" ("id");

ALTER TABLE "subscribers" ADD FOREIGN KEY ("cur_plan_id") REFERENCES "Plans" ("id");
