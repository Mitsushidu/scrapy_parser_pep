import csv
import datetime as dt
from collections import defaultdict

from pep_parse.settings import BASE_DIR


class PepParsePipeline:
    def open_spider(self, spider):
        self.filepath = BASE_DIR / 'results'
        self.status_count = defaultdict(int)

    def process_item(self, item, spider):
        self.status_count[item['status']] += 1
        return item

    def close_spider(self, spider):
        current_datetime = dt.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = f'status_summary_{current_datetime}.csv'
        self.status_count['Total'] = sum(self.status_count.values())
        with open(
            self.filepath / filename,
            mode='w',
            encoding='utf-8',
            newline=''
        ) as f:
            writer = csv.writer(
                f,
                delimiter=' ',
                quotechar='|'
            )
            writer.writerow(['Статус', 'Количество'])
            writer.writerows(self.status_count.items())
