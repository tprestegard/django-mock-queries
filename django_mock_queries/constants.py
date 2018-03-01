from pydoc import locate

COMPARISON_EXACT = 'exact'
COMPARISON_IEXACT = 'iexact'
COMPARISON_CONTAINS = 'contains'
COMPARISON_ICONTAINS = 'icontains'
COMPARISON_GT = 'gt'
COMPARISON_GTE = 'gte'
COMPARISON_LT = 'lt'
COMPARISON_LTE = 'lte'
COMPARISON_IN = 'in'
COMPARISON_STARTSWITH = 'startswith'
COMPARISON_ISTARTSWITH = 'istartswith'
COMPARISON_ENDSWITH = 'endswith'
COMPARISON_IENDSWITH = 'iendswith'
COMPARISON_ISNULL = 'isnull'
COMPARISON_REGEX = 'regex'
COMPARISON_IREGEX = 'iregex'
COMPARISON_DATE = 'date'
COMPARISON_YEAR = 'year'
COMPARISON_MONTH = 'month'
COMPARISON_DAY = 'day'
COMPARISON_WEEK_DAY = 'week_day'
COMPARISON_HOUR = 'hour'
COMPARISON_MINUTE = 'minute'
COMPARISON_SECOND = 'second'
COMPARISON_RANGE = 'range'
COMPARISONS = (
    COMPARISON_EXACT,
    COMPARISON_IEXACT,
    COMPARISON_CONTAINS,
    COMPARISON_ICONTAINS,
    COMPARISON_GT,
    COMPARISON_GTE,
    COMPARISON_LT,
    COMPARISON_LTE,
    COMPARISON_IN,
    COMPARISON_STARTSWITH,
    COMPARISON_ISTARTSWITH,
    COMPARISON_ENDSWITH,
    COMPARISON_IENDSWITH,
    COMPARISON_ISNULL,
    COMPARISON_REGEX,
    COMPARISON_IREGEX
)
DATE_COMPARISONS = (
    COMPARISON_DATE,
    COMPARISON_YEAR,
    COMPARISON_MONTH,
    COMPARISON_DAY,
    COMPARISON_WEEK_DAY,
)
DATETIME_COMPARISONS = (
    COMPARISON_DATE,
    COMPARISON_YEAR,
    COMPARISON_MONTH,
    COMPARISON_DAY,
    COMPARISON_WEEK_DAY,
    COMPARISON_HOUR,
    COMPARISON_MINUTE,
    COMPARISON_SECOND,
)

MONTH_BOUNDS = (1, 12)
DAY_BOUNDS = (1, 31)
WEEK_DAY_BOUNDS = (1, 7)
HOUR_BOUNDS = (0, 23)
MINUTE_BOUNDS = (0, 59)
SECOND_BOUNDS = (0, 59)

CONNECTORS_OR = 'OR'
CONNECTORS_AND = 'AND'
CONNECTORS = (
    CONNECTORS_OR,
    CONNECTORS_AND,
)

AGGREGATES_SUM = 'SUM'
AGGREGATES_COUNT = 'COUNT'
AGGREGATES_MAX = 'MAX'
AGGREGATES_MIN = 'MIN'
AGGREGATES_AVG = 'AVG'
AGGREGATES = (
    AGGREGATES_SUM,
    AGGREGATES_COUNT,
    AGGREGATES_MAX,
    AGGREGATES_MIN,
    AGGREGATES_AVG,
)

DjangoQ = locate('django.db.models.Q')
DjangoQuerySet = locate('django.db.models.QuerySet')
DjangoDbRouter = locate('django.db.router')
DjangoModelDeletionCollector = locate('django.db.models.deletion.Collector')
ObjectDoesNotExist = locate('django.core.exceptions.ObjectDoesNotExist')
MultipleObjectsReturned = locate('django.core.exceptions.MultipleObjectsReturned')
