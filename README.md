# Delta Lake

Some example notebooks on how to use the delta lake

Introduction:
https://docs.delta.io/latest/delta-intro.html

Most relevant (quite subjective):
* Upserts and deletes: update / delete rows that change.
* Time travel: being able to go back before updates / deletes (for example if updated data are faulty)


When time travel does make sense:
* We have a table with updates / appends / deletions of rows.
* We are only interested in the most recent data, i.e. if a row is updated, the old value is not of interest any more.
* However, we are afraid to just overwrite the old data because new data might be faulty and we want to be able to recover the old data in that case.
* However, we need to be able to reproduce the old state, for example to debug potential inconsistencies reported by users.

When time travel does not make sense:
* We scrape data daily and are interested in the "history" of the data
    * bad idea: upsert data and then use time travel to loop through history
    * better: append data as new events.
