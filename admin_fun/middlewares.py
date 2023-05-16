# В этом файле будут лежать все используемые мидлвари (их будет всего две)
from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware
from aiogram import types

class LimitedRequestsMiddleware(LifetimeControllerMiddleware):
    def __init__(self, max_requests_per_day=15, **kwargs):
        self.max_requests_per_day = max_requests_per_day
        super().__init__(**kwargs)

    async def on_pre_process_update(self, update, data):
        user_id = update.message.from_user.id
        db_data = {'num_requests': 0, 'last_request_datetime': None}
        data.setdefault('user_requests', {})

        if user_id in data['user_requests']:
            db_data = data['user_requests'][user_id]

        if db_data['last_request_datetime'] and not is_24_hours_passed(db_data['last_request_datetime']):
            if db_data['num_requests'] >= self.max_requests_per_day:
                await update.message.reply('Превышено количество запросов в день.')
                raise StopPropagation

        db_data['num_requests'] += 1
        db_data['last_request_datetime'] = datetime.datetime.now()
        data['user_requests'][user_id] = db_data

class LimitedRequestsMiddleware_min(LifetimeControllerMiddleware):
    def __init__(self, delay_minutes=2, **kwargs):
        self.delay_minutes = delay_minutes
        super().__init__(**kwargs)

    async def on_pre_process_update(self, update: types.Update, data: dict):
        user_id = update.message.from_user.id
        db_data = {'last_request_datetime': None}
        data.setdefault('user_requests', {})

        if user_id in data['user_requests']:
            db_data = data['user_requests'][user_id]

        if db_data['last_request_datetime'] and not is_delay_passed(db_data['last_request_datetime']):
            await update.message.reply('Превышено количество запросов в 2 минуты.')
            raise StopPropagation

        db_data['last_request_datetime'] = datetime.datetime.now()
        data['user_requests'][user_id] = db_data

def is_delay_passed(last_request_datetime):
    delay = datetime.timedelta(minutes=2)
    return (datetime.datetime.now() - last_request_datetime) > delay