import csv
import datetime as dt
from pep_parse.settings import BASE_DIR


class PepParsePipeline:
    def open_spider(self, spider):
        self.filepath = BASE_DIR / 'results'
        self.status_count = {}

    def process_item(self, item, spider):
        if item['status'] not in self.status_count.keys():
            self.status_count[item['status']] = 1
        else:
            self.status_count[item['status']] += 1
        return item

    def close_spider(self, spider):
        current_datetime = dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f'status_summary_{current_datetime}.csv'
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
            for key in self.status_count.keys():
                writer.writerow([key, self.status_count[key]])
            writer.writerow(['Total', sum(self.status_count.values())])
