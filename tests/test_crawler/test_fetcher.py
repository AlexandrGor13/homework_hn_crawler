import pytest
from crawler.fetcher import PageFetcher


@pytest.mark.asyncio
async def test_fetch_hn_homepage(fetcher):
    html = await fetcher.fetch_hn_page()
    assert "<title>Hacker News</title>" in html


@pytest.mark.asyncio
async def test_fetcher_lifecycle():
    pf = PageFetcher()
    assert pf.session is None

    await pf.start()
    assert pf.session is not None

    await pf.close()
    assert pf.session.closed
