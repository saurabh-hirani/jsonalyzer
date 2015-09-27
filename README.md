# jsonalyzer

Because one life is too short to write boilerplate json again and again. Work in progress.

All examples need a url serving sample json. Use https://github.com/saurabh-hirani/jsonserver to run a simple json server or replace the port and uri in the examples accordingly.

* Examples

- Check if the url is valid

````
$ cat > /var/tmp/test.json
  {"this": "that"}

$ ./jsonalyzer -H localhost -p 5555 --uri /json/var/tmp/test.json
````

- Check if the url returns a json which contains a key 'this'

````
$ ./jsonalyzer -H localhost -p 5555 \
                            --uri /json/var/tmp/test.json \
                            --match_key this
````

- Check if the json key 'this' has a value 'that'

````
$ ./jsonalyzer -H localhost -p 5555 \
                            --uri /json/var/tmp/test.json \
                            --match_key_val this:that
````

- Check non-existent key

````
$ ./jsonalyzer -H localhost -p 5555 \
                            --uri /json/var/tmp/test.json \
                            --match_key doesnotexist
````

- Check non-existent key, value pair

````
$ ./jsonalyzer -H localhost -p 5555 \
                            --uri /json/var/tmp/test.json \
                            --match_key_val doesnotexist:doesnotexist
````

- If the value is a number, check if it is within the warning and critical limits

````
$ cat > /var/tmp/limits.json
  {"curr_val": 75}

$ ./jsonalyzer -H localhost -p 5555 \
                            --uri /json/var/tmp/limits.json \
                            --match_key curr_val \
                            --warning 50 \
                            --critical 80

$ ./jsonalyzer -H localhost -p 5555 \
                            --uri /json/var/tmp/limits.json \
                            --match_key curr_val \
                            --warning 50 \
                            --critical 70
````

- If your check goes beyond the usual existence and numerical comparison you can write a callback which is passed the program options and the json


````
$ cat > /var/tmp/nkeys.json
  {"a": 1, "b": 2, "c": 3}

$ ./jsonalyzer -H localhost -p 5555 \
                            --uri /json/var/tmp/nkeys.json \
                            --callback_path json_callbacks.py \
                            --callback_func check_nkeys \
                            --warning 1 \
                            --critical 2
````
