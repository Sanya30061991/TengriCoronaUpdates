import logging
from aiogram import Bot, Dispatcher, executor, types
from but import *
from parse import *
from database import *
import asyncio
from datetime import datetime


TOKEN = ''
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    if db_get('tel_id',str(message.from_user.id))==None:
        db_insert(str(message.from_user.id))
        await message.answer('Choose your language:', reply_markup=keyboarr)
    elif db_get('tel_id',str(message.from_user.id))!=None and db_get('tel_id',str(message.from_user.id))[3]=='english':
        await message.answer('Доброго времени суток, {message.from_user.first_name}! \nСкорее всего, ты уже знаешь о том что творится в мире: о коронавирусе, количестве заболевших и выздоровевших, о состоянии ЧС, действующем на территории нашей страны, об условиях самоизоляции. Данный бот предлагает тебе СОВЕРШЕННО БЕСПЛАТНУЮ подписку на обновления и новости, касательно этой злосчастной китайской инфекции.')
    elif db_get('tel_id',str(message.from_user.id))!=None and db_get('tel_id',str(message.from_user.id))[3]=='russian':
        string = f'Nice to meet you, {message.from_user.first_name}! \nWe think you should already know about consistense of the world: about coronavirus, amount of infected and healed people, state of emergency in your country and selfisolation conditions. This bot provides ABSOLUTELY FREE subscription on updates and news, related to this chinese infection.'
        await message.answer(string)
@dp.message_handler(commands=['subscribe'])
async def send_sb(message: types.Message):
    if db_get('tel_id',str(message.from_user.id))!=None and db_get('tel_id',str(message.from_user.id))[3]=='english' and db_get('tel_id',str(message.from_user.id))[2]=='FALSE':
        db_update('tel_id',str(message.from_user.id),'sub','TRUE')
        await message.answer('Subsciption accepted. Be await for news and stay safe!')
    elif db_get('tel_id',str(message.from_user.id))!=None and db_get('tel_id',str(message.from_user.id))[3]=='russian' and db_get('tel_id',str(message.from_user.id))[2]=='FALSE':
        db_update('tel_id',str(message.from_user.id),'sub','TRUE')
        await message.answer('Подписка оформлена. Ожидайте новостей и оставайтесь дома!')
    elif db_get('tel_id',str(message.from_user.id))!=None and db_get('tel_id',str(message.from_user.id))[3]=='russian' and db_get('tel_id',str(message.from_user.id))[2]=='TRUE':
        await message.answer('Подписка уже была оформлена.')
    elif db_get('tel_id',str(message.from_user.id))!=None and db_get('tel_id',str(message.from_user.id))[3]=='english' and db_get('tel_id',str(message.from_user.id))[2]=='TRUE':
        await message.answer('Subscription has been already confirmed.')
@dp.message_handler(commands=['unsubscribe'])
async def send_unsb(message: types.Message):
    if db_get('tel_id',str(message.from_user.id))!=None and db_get('tel_id',str(message.from_user.id))[3]=='english' and db_get('tel_id',str(message.from_user.id))[2]=='TRUE':
        db_update('tel_id',str(message.from_user.id),'sub','FALSE')
        await message.answer('Subsciption cancelled.')
    elif db_get('tel_id',str(message.from_user.id))!=None and db_get('tel_id',str(message.from_user.id))[3]=='russian' and db_get('tel_id',str(message.from_user.id))[2]=='TRUE':
        db_update('tel_id',str(message.from_user.id),'sub','FALSE')
        await message.answer('Подписка отменена.')
    elif db_get('tel_id',str(message.from_user.id))!=None and db_get('tel_id',str(message.from_user.id))[3]=='russian' and db_get('tel_id',str(message.from_user.id))[2]=='FALSE':
        await message.answer('Подписка уже была отменена.')
    elif db_get('tel_id',str(message.from_user.id))!=None and db_get('tel_id',str(message.from_user.id))[3]=='english' and db_get('tel_id',str(message.from_user.id))[2]=='FALSE':
        await message.answer('Subscription has been already cancelled.')
@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    if db_get('tel_id',str(message.from_user.id))[3]=='english':
        await message.answer('LIST OF COMMANDS:\n\n/start - starts the bot\n/help - get list of commands\n/latest - get the latest announce from Tengrinews.kz about corona\n/subscribe - subscribe to updates\n/unsubscribe - unsubscribe from updates\n/language - changing language')
    elif db_get('tel_id',str(message.from_user.id))[3]=='russian':
        await message.answer('СПИСОК ДОСТУПНЫХ КОММАНД:\n\n/start - запустить бота\n/help - получить список доступных комманд\n/latest - получить последнюю новость, связанную с коронавирусом с портала Tengrinews.kz\n/subscribe - подписаться на новостную ленту\n/unsubscribe - отписаться от новостной ленты\n/language - смена языка')
@dp.message_handler(commands=['latest'])
async def send_new(message: types.Message):
    ark, _ = parsing()
    url = HOST+ark['img']
    title = ark['title']
    content = ark['content']
    link = ark['link']
    await message.answer_photo(url, f'{title}.\n\n{content}\n\n\nЧитать далее...\n{HOST}{link}')
@dp.message_handler(commands=['language'])
async def send_lang(message: types.Message):
    if db_get('tel_id',str(message.from_user.id))[3]=='english':
        await message.answer('Choose language. ',reply_markup=keyboarr)
    elif db_get('tel_id',str(message.from_user.id))[3]=='russian':
        await message.answer('Выберите язык. ',reply_markup=keyboarr)

@dp.message_handler(text ='Русский')
async def send_wlcm1(message: types.Message):
    db_update('tel_id',str(message.from_user.id),'lang','russian')
    string = f'Доброго времени суток, {message.from_user.first_name}! \nСкорее всего, ты уже знаешь о том что творится в мире: о коронавирусе, количестве заболевших и выздоровевших, о состоянии ЧС, действующем на территории нашей страны, об условиях самоизоляции. Данный бот предлагает тебе СОВЕРШЕННО БЕСПЛАТНУЮ подписку на обновления и новости, касательно этой злосчастной китайской инфекции.'
    await message.answer(string)
@dp.message_handler(text ='English')
async def send_wlcm2(message: types.Message):
    db_update('tel_id',str(message.from_user.id),'lang','english')
    string = f'Nice to meet you, {message.from_user.first_name}! \nWe think you should already know about consistense of the world: about coronavirus, amount of infected and healed people, state of emergency in your country and selfisolation conditions. This bot provides ABSOLUTELY FREE subscription on updates and news, related to this chinese infection.'
    await message.answer(string)
async def scheduled(wat):
    while True:
        await asyncio.sleep(wat)
        a, con = parsing()
        if con=='no':
            arr = db_get_all('sub','TRUE')
            url = HOST+a['img']
            title = a['title']
            content = a['content']
            link = a['link']
            for item in arr:
                await bot.send_photo(
                    str(item[1]),
                    url, 
                    caption = title +"\n\n" + content + "\n\n\nЧитать далее...\n" + HOST+link,
                    )



if __name__ == '__main__':
    dp.loop.create_task(scheduled(1800))
    executor.start_polling(dp, skip_updates=True)