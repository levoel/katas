CREATE FUNCTION
  agecalculator(
    age DATE
  )
    RETURNS
      INTEGER AS $$
BEGIN
    RETURN 
      date_part('year', AGE(age))
    ;
END
$$ LANGUAGE plpgsql
;
