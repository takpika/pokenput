from setuptools import setup, find_packages

setup(
    name='pokenput',
    version="0.0.1",
    description="ポケモンのキーボードの自動入力ツール",
    long_description="初代ポケモンのキーボードの自動入力ツールです",
    url='https://takpikamcs.pgw.jp',
    author='takpika',
    author_email='contact@takpikamcs.pgw.jp',
    license='none',
    classifiers=[
    ],
    keywords='pokemon',
    install_requires=["pyautogui", "time"],
)