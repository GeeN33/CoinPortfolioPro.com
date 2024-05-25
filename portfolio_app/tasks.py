from celery import shared_task

from portfolio_app.services import CalculatePortfolio, EventPortfolio, EventUpdata, Loading_To_bd, Top10


@shared_task
def calculate_portfolio():
    CalculatePortfolio()
    return 'calculate portfolio Ok'

@shared_task
def event_portfolio():
    EventPortfolio()
    return 'event portfolio Ok'

@shared_task
def calculate_event():
    CalculatePortfolio()
    EventPortfolio()
    return 'calculate event Ok'

@shared_task
def event_updata():
    EventUpdata()
    return 'event updata Ok'

@shared_task
def loading_to_bd():
    Loading_To_bd()
    return 'loading to bd Ok'

@shared_task
def top_10():
    Top10()
    return 'top 10 Ok'


# celery -A core worker -l info --pool=solo
#  celery -A core beat -l INFO

  # . core.celery.debug_task
  # . portfolio_app.tasks.calculate_portfolio
  # . portfolio_app.tasks.event_portfolio
  # . portfolio_app.tasks.event_updata
  # . portfolio_app.tasks.calculate_event
  # . portfolio_app.tasks.loading_to_bd
  # . portfolio_app.tasks.top_10


