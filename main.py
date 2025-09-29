import asyncio
import json

from crawl4ai import *

async def main():
    schema = {
        "name": "gongwuyuan",
        "baseSelector": '//*[@id="printcontent"]',
        "baseFields":[
            { "name": "title", "selector": ".//h3", "type": "text"}
        ],
        "fields": [
            {
                "name": "title1",
                "selector": './/h3',
                "type": "text"
            },
            {
                "name": "subtitle",
                "selector": './/div[1]/div/div[@class="col-xs-12 subtitle"]',
                "type": "text"
            },
            {
                "name": "content",
                "selector": ".article-content",
                "type": "html"
            }
        ]
    }

    extract_strategy = JsonXPathExtractionStrategy(schema=schema, verbose=True)
    config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        extraction_strategy=extract_strategy,
    )
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://www.gkzenti.cn/paper/1758335703342",
            config=config
        )
        if not result.success:
            print('!!!! Failed to extract data:', result.error_message)
            return
        # print(result.markdown)
        data = json.loads(result.extracted_content)
        print('===>', data)


if __name__ == "__main__":
    asyncio.run(main())