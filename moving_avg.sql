select *,
  avg(Price) OVER(ORDER BY Date
     ROWS BETWEEN 2 PRECEDING AND CURRENT ROW )
     as moving_average
from stock_price;


# 30 day moving avg

select *,
  avg(Price) OVER(ORDER BY Date
      ROWS BETWEEN 1 PRECEDING AND CURRENT ROW )
     as 2day_moving_average,
  avg(Price) OVER(ORDER BY Date
      ROWS BETWEEN 29 PRECEDING AND CURRENT ROW )
      as 30day_moving_average
from stock_price;

SELECT *,
      avg(confirmed_day) OVER(
          PARTITION BY country
          ORDER BY date
          ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)
          AS 7day_moving_average
FROM confirmed_covid;