# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv

load_dotenv()

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# Netscape HTTP Cookie File
# http://curl.haxx.se/rfc/cookie_spec.html
# This is a generated file!  Do not edit.

.instagram.com	TRUE	/	TRUE	1775207442	datr	EizAZzNBWzPAUy6AI1N-OmDs
.instagram.com	TRUE	/	TRUE	1772183442	ig_did	34768769-DE82-4FFF-8AB3-13CE863E606D
.instagram.com	TRUE	/	TRUE	1775207443	mid	Z8AsEgABAAHhz84zfct7TH6RsiWy
.instagram.com	TRUE	/	TRUE	1772183482	ig_nrcb	1
.instagram.com	TRUE	/	TRUE	1775208370	ps_l	1
.instagram.com	TRUE	/	TRUE	1775208370	ps_n	1
.instagram.com	TRUE	/	TRUE	1773688946	csrftoken	uEQJnPbaol6hyqTnc5gO5I5bVkg6XIJH
.instagram.com	TRUE	/	TRUE	1750015346	ds_user_id	57315762401
.instagram.com	TRUE	/	TRUE	1742844146	dpr	2.8125
.instagram.com	TRUE	/	TRUE	1773775190	sessionid	57315762401%3A47HHNKcCiljZJx%3A18%3AAYcRkaF7ga792ZXbBCvS6Tulx9T86EcZ2PzaM307bA
.instagram.com	TRUE	/	TRUE	1742844146	wd	384x746
.instagram.com	TRUE	/	TRUE	0	rur	"HIL\05457315762401\0541773775346:01f77358fe8aec5bf97d87037687bb95736a8262400a2630257739d794264d635703bd01"
"""

YTUB_COOKIES = """
# Netscape HTTP Cookie File
# https://curl.haxx.se/rfc/cookie_spec.html
# This is a generated file! Do not edit.

.youtube.com	TRUE	/	TRUE	1757791102	VISITOR_INFO1_LIVE	gCssxhnEkms
.youtube.com	TRUE	/	TRUE	1757791102	VISITOR_PRIVACY_METADATA	CgJJThIEGgAgYQ%3D%3D
.youtube.com	TRUE	/	TRUE	1757791102	__Secure-ROLLOUT_TOKEN	CLP3qbip35_FyQEQw6iV5b2yiwMY_I-ttuqRjAM%3D
.youtube.com	TRUE	/	TRUE	1776799103	PREF	f6=40000000&tz=Asia.Dhaka&f5=30000&f7=100
.youtube.com	TRUE	/	TRUE	1739036076	YTSESSION-rvkia	ANPz9Kj3xjV046Wm9xkEWGShlqjYt2FRcG7oa3LU7wzPobCY/HOM+SaffZonw2BmeOfbp39YP3BpXTV0we+ju7Mz2KKvJtgh4VQ6OeVUQvDMYQUCcxxF0JAdQrzovBaMVNPmcZT2wWyJFKT192jQChAgBDSYNQJZ2K92m8ZpVoa1HAAd2jjbtnW511+0huWMsPkU3Jz+15lY0YO3pUbYO0nQYo4wyofWy+f9zUgECmviArXlfjXftefDgjc0Yuz0kCPcSoGkwEVPBLf3eQj2Dhd0FSGLAlgeq5zIPftITAq6h89L5Bh52XXJxULO9M0p26VFpnl5XVnFFjTlJJFNtb7aWCxsY5DCgIyX2Dv1Li4=
.youtube.com	TRUE	/	TRUE	1739037756	GPS	1
.youtube.com	TRUE	/	TRUE	1770571968	__Secure-1PSIDTS	sidts-CjIBEJ3XVyhqi7CNBjVTbXJ3bfKjWEfZfblJIDWXryFzhvipZMMG5BQqD51JeDWXtboBCBAA
.youtube.com	TRUE	/	TRUE	1770571968	__Secure-3PSIDTS	sidts-CjIBEJ3XVyhqi7CNBjVTbXJ3bfKjWEfZfblJIDWXryFzhvipZMMG5BQqD51JeDWXtboBCBAA
.youtube.com	TRUE	/	FALSE	1776799102	HSID	Ah75MiG13AIp14hFv
.youtube.com	TRUE	/	TRUE	1776799102	SSID	AC1VphNI1K3vv6itX
.youtube.com	TRUE	/	FALSE	1776799102	APISID	OzS34f3y8cLNW2df/AG3F9T06_18CpTxga
.youtube.com	TRUE	/	TRUE	1776799102	SAPISID	h_y2Cx-Rq6Wqon2R/AenFblpGKRPo0hib-
.youtube.com	TRUE	/	TRUE	1776799102	__Secure-1PAPISID	h_y2Cx-Rq6Wqon2R/AenFblpGKRPo0hib-
.youtube.com	TRUE	/	TRUE	1776799102	__Secure-3PAPISID	h_y2Cx-Rq6Wqon2R/AenFblpGKRPo0hib-
.youtube.com	TRUE	/	FALSE	1776799102	SID	g.a000uwglungMfmNyEQ2ptCnQ6qmlIecJaIh6zzDvxCJ3Xl-hYvQS3HYtxnOzRiu2lLzi3UfPpAACgYKAdASAQASFQHGX2MiqfrHztIKQ8FAvEdGg_sc_xoVAUF8yKqsqXWMAyMjPTzbzEiIb88g0076
.youtube.com	TRUE	/	TRUE	1776799102	__Secure-1PSID	g.a000uwglungMfmNyEQ2ptCnQ6qmlIecJaIh6zzDvxCJ3Xl-hYvQS-s82A_LcyQVAWOIQYpBcXwACgYKAcQSAQASFQHGX2MiguwNFoj0pztgBRlKQL_MVhoVAUF8yKr2rHbuQDg8qEt5-q6pBnMU0076
.youtube.com	TRUE	/	TRUE	1776799102	__Secure-3PSID	g.a000uwglungMfmNyEQ2ptCnQ6qmlIecJaIh6zzDvxCJ3Xl-hYvQSPP7f0R76TAaSocPcQ0u50QACgYKAawSAQASFQHGX2Miqeuip6EyMWGsKbcWQTqhMRoVAUF8yKo124ejqzgKfS-YDXErckC-0076
.youtube.com	TRUE	/	FALSE	1773775111	SIDCC	AKEyXzWzrEulFC-aMyDxEFIIRqjMkZSikI8Wm-nZUbh8fc80jrJ7elp-q8CsOdxS3pXBjHGg
.youtube.com	TRUE	/	TRUE	1773775111	__Secure-1PSIDCC	AKEyXzV3kqD1YerE1-PwSzrL7LW0xTCGtS8mnvjFBvrxXo5Gzuxcrjm_aekN55BlY_d9RoRj
.youtube.com	TRUE	/	TRUE	1773775111	__Secure-3PSIDCC	AKEyXzUZIfZaOBIs8v0NpbX_AjOFoBvYSTk21HPOTTZzOE3TCmTr9ruUxFvyZW140mIpR-GSmg
.youtube.com	TRUE	/	TRUE	1773595969	LOGIN_INFO	AFmmF2swRAIgILLRf59yIChD2gKlWTFsBYjnDXR0IG0I4TEQx1fPfFUCIEgPvpH_bqETX-hezF0DNGKdT-MbctGc0zxurk0-Regx:QUQ3MjNmd3Bxc1Y2S3hBcmY1MW5VLVg1cGpFZmd0eW9kck9WSXJWZ2xrZ2VCRGxLeE5VSEZoTExwTnRqZXVFNUt1NHNDQ3ZxbjZJaU5yd2VHdEcwZnVhQlExcGRJQVB2QUlXRk4zZEs1NnNnX0cyWGIwWmEzNzBFdmVXTHQ4X1YzOHVsZURDRE9jTXdMM19PRGs4ZUhLdGh2MTlJME14VDh3
.youtube.com	TRUE	/	FALSE	1739035982	ST-mv8dsf	csn=1kCbFKeMTFV8h4Nf&itct=CIgBEPxaIhMI6bba6c20iwMVAGv1BR2R9AOqMgpnLWhpZ2gtcmVjWg9GRXdoYXRfdG9fd2F0Y2iaAQYQjh4YngE%3D
.youtube.com	TRUE	/	FALSE	1740588509	ST-5iat4b	csn=i7dlUJZOrG2N-Q5n&itct=CEYQ_FoiEwj99Ly15eGLAxWJvksFHQpsHREyCmctaGlnaC1yZWNaD0ZFd2hhdF90b193YXRjaJoBBhCOHhieAQ%3D%3D
.youtube.com	TRUE	/	FALSE	1740588510	ST-bkav5f	csn=i7dlUJZOrG2N-Q5n&itct=CDwQ_FoiEwj99Ly15eGLAxWJvksFHQpsHREyCmctaGlnaC1yZWNaD0ZFd2hhdF90b193YXRjaJoBBhCOHhieAQ%3D%3D
.youtube.com	TRUE	/	TRUE	0	YSC	CBTcBjzsA7A
"""

API_ID = os.getenv("API_ID", "")
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
MONGO_URI = os.getenv("MONGO_DB", "")
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "6863006030").split())) # list seperated via space
DB_NAME = os.getenv("DB_NAME", "telegram_downloader")
STRING = os.getenv("STRING", None) # optional
LOG_GROUP = int(os.getenv("LOG_GROUP", "-1002263306015")) # optional with -100
FORCE_SUB = int(os.getenv("FORCE_SUB", "-1001775343398")) # optional with -100
MASTER_KEY = os.getenv("MASTER_KEY", "gK8HzLfT9QpViJcYeB5wRa3DmN7P2xUq") # for session encryption
IV_KEY = os.getenv("IV_KEY", "s7Yx5CpVmE3F") # for decryption
YT_COOKIES = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)
