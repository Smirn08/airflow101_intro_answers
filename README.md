# Ответы на [задачи](https://gist.github.com/Melevir/478d5fc40301d4d95f3f9dc63a65b402#%D0%B7%D0%B0%D0%B4%D0%B0%D1%87%D0%B8)

## Насколько похорошела Москва
1. Получить `API_KEY` [тут](https://apidata.mos.ru/Account/Manage)
> Подробнее: [apidata.mos.ru/Docs](https://apidata.mos.ru/Docs)
2. Вбить свой `API_KEY` в `mosru_api.ini`
3. Запустить скрипт для просмотра результата
    ```bash
    pip3 install -r requirements.txt
    python3 wifi_counter.py
    ```

### Ответ:
![](https://sun9-23.userapi.com/c855036/v855036182/2341f3/gFybliyfSVg.jpg)

***

## Статистика оказаний услуг

```sql
SELECT type, count(type) AS count
FROM doc
GROUP BY type
ORDER BY count DESC
LIMIT 10;
```

***

## Обновить python до 3.8
```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.8
```
*но я этого делать не буду :>*