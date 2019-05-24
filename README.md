# Search phone number

## Description
This project can help you find needed phone numbers if you know the first digits. It is based on Suffix Tree.
Before run script, create file 'numbers.txt' and fill it.

## For example 'numbers.txt':
```bash
380672832505
380671232530
380675683254
380672831230
380672832503
380671323220
380672836400
380675632234
380672823457
38067dfses24
380671657650
380674646346
380536235324
389675753463
385634554553
380534646532
380436235353
38067dfss254
38067dfses24 
```

## Run searching
```bash
python3.6 search.py --search <first digits>
```

## Show numbers
You can show all phone numbers, where will be found needed numbers.
```bash
python3.6 search.py --show
```
## Test
```bash
pytest test.py -vv
```

## Help
If you have some problems:
```bash
python3.6 search.py --help
```


