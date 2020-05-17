import discord
token = 'token'
client = discord.Client()

@client.event
async def on_ready():
    print('봇이 시작되었습니다! 로그인 아이디:')
    print(client.user.name)
    print(client.user.id)
    print('====================================')

@client.event
async def on_message(message):
    if message.content == '하이':
        await message.channel.send('안녕하세요!')
    if message.content == '심심해':
        await message.channel.send('아무거나 하세요')
    if message.content == '심심':
        await message.channel.send('아무거나 하세요')
    if message.content == 'ㄱㅁㄴ':
        await message.channel.send('좋은아침!')
    if message.content == '긋모닝':
        await message.channel.send('좋은아침!')
    if message.content == 'm.미로':
        await message.channel.send('https://www.youtube.com/channel/UC9kVMJFsPOY6YWUvCRAs08A?view_as=subscriber')
    if message.content == 'm.충무김밥':
        await message.channel.send('https://www.youtube.com/channel/UCpPodoPAmow94ubTZe6YRlg')
    if message.content == 'm.베리':
        await message.channel.send('https://www.youtube.com/channel/UCO2Z24XXzcDC7Rpmtfbo9jA')
    if message.content == 'm.마뱀':
        await message.channel.send('https://www.youtube.com/channel/UCXb_FH_cJQobc-QvGSe9O-Q')
    if message.content == 'm.클론':
        await message.channel.send('https://www.youtube.com/channel/UCVx3jf44V9rUkfrmQL_g0JQ')
    if message.content == 'm.명령어':
        await message.channel.send('하이 m.마뱀m.충무김밥m.베리m.클론m.미로m제작자')
    if message.content == 'm.제작자':
        await message.channel.send('미로')

client.run(token)
