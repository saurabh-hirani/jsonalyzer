# jsonchecker

Because one life is too short to write boilerplate json again and again. Work in progress.

All examples need a url serving sample json. Use https://github.com/saurabh-hirani/jsonserver to run a simple json server.

* Examples

````
  $ cat > /var/tmp/test.json
    {"this": "that"}

  $ ./jsonchecker -H localhost -p 5555 --uri /json/var/tmp/test.json

  $ ./jsonchecker -H localhost -p 5555 --uri /json/var/tmp/test.json --match_key this

  $ ./jsonchecker -H localhost -p 5555 --uri /json/var/tmp/test.json \
                  --match_key_val this:that

  $ ./jsonchecker -H localhost -p 5555 --uri /json/var/tmp/test.json --match_key doesnotexist

  $ ./jsonchecker -H localhost -p 5555 --uri /json/var/tmp/test.json --match_key_val doesnotexist:doesnotexist

  $ cat > /var/tmp/limits.json
    {"curr_val": 75}

  $ ./jsonchecker -H localhost -p 5555 --uri /json/var/tmp/limits.json --match_key curr_val --warning 50 --critical 80

  $ ./jsonchecker -H localhost -p 5555 --uri /json/var/tmp/limits.json --match_key curr_val --warning 50 --critical 70

  $ cat > /var/tmp/nkeys.json
    {"a": 1, "b": 2, "c": 3}

  $ ./jsonchecker -H localhost -p 5555 --uri /json/var/tmp/nkeys.json --callback_path json_callbacks.py --callback_func check_nkeys --warning 1 --critical 2
````
