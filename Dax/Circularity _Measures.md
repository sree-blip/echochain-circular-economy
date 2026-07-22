# Circularity Measures

## Average Circularity Score

```DAX
Average Circularity Score =
AVERAGE('circularity_score_updated'[overall_circularity_score])
```

## Circularity Target

```DAX
Circularity Target = 80
```

## Circularity Gap

```DAX
Circularity Gap =
[Circularity Target] - [Average Circularity Score]
```

## Circularity Status

```DAX
Circularity Status =
SWITCH(
    TRUE(),
    [Average Circularity Score] >= 80, "Excellent",
    [Average Circularity Score] >= 60, "Moderate",
    "Needs Improvement"
)
```
