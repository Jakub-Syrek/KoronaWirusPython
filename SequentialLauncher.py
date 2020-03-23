import ScraperPolska
import LoadDataToSql
import importlib
import time
from timeloop import Timeloop
from datetime import timedelta

tl = Timeloop()

@tl.job(interval=timedelta(hours=6))
def RecurrentTasks():
    importlib.reload(ScraperPolska)
    LoadDataToSql

if __name__ == "__main__":
    tl.start(block=True)
