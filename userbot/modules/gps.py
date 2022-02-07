# credits: mrconfused
from geopy.geocoders import Nominatim
from telethon.tl import types

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.gps(?: |$)(.*)")
async def gps(event):
    if event.fwd_from:
        return
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    input_str = event.pattern_match.group(1)

    if not input_str:
        return await event.edit("`Mohon Berikan Tempat Yang Dicari`")

    await event.edit("`Menemukan Lokasi Ini Di Server Map....`")

    geolocator = Nominatim(user_agent="Geez")
    if geoloc := geolocator.geocode(input_str):
        lon = geoloc.longitude
        lat = geoloc.latitude
        await reply_to_id.reply(
            input_str, file=types.InputMediaGeoPoint(types.InputGeoPoint(lat, lon))
        )
        await event.delete()
    else:
        await event.edit("`Saya Tidak Dapat Menemukannya`")


CMD_HELP.update({"gps": ">.`gps`" "\nUsage: Untuk Mendapatkan Lokasi Map"})
