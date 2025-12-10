import argparse
import logging

from crawler.crawler import HNCrawler
from crawler.settings import crawl_interval


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--once', action='store_true',
                        help='Run single crawl cycle')
    parser.add_argument('--interval', type=int,
                        default=crawl_interval,
                        help='Crawl interval in seconds (min 5 sec)')
    parser.add_argument('--log-level',
                        choices=['DEBUG','INFO','WARNING','ERROR'],
                        default='INFO')
    parser.add_argument('--show', type=int, metavar='N',
                        help='Show last N news items')

    args = parser.parse_args()
    if args.interval < 5:
        parser.error("Interval must be >= 5 seconds")

    return args


async def main():
    args = parse_args()

    logging.getLogger().setLevel(args.log_level)

    crawler = HNCrawler(interval=args.interval)
    try:
        if args.show:
            await crawler.show_recent_news(args.show)
        else:
            await crawler.run(run_once=args.once)
    except KeyboardInterrupt:
        logging.info("Graceful shutdown")

