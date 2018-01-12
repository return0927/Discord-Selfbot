from cx_Freeze import setup, Executable

setup(name="디스코드 셀프봇",
      version="1.0",
      description="토큰을 이용하여 디스코드에 접근하고, 각종 커맨드기능을 사용합니다.",
      author="return0927",
      executables=[Executable("bot.py")],
      options={
          "build_exe": {"packages": ["asyncio", "jinja2", "discord", "requests", "random"]}
      }
      )
