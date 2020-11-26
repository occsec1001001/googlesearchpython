# Using python to scrape links from a google search, useful when using the search params for filetype:### to collate a list of files which you can then download via normal general bash loops if you so wish... 


googlesearch.search(query, tld='com', lang='en', tbs='0', safe='off', num=10, start=0, stop=None, pause=2.0, country='', extra_params=None, user_agent=None, verify_ssl=True)[source]

    Search the given query string using Google.
    Parameters:	

        query (str) – Query string. Must NOT be url-encoded.
        tld (str) – Top level domain.
        lang (str) – Language.
        tbs (str) – Time limits (i.e “qdr:h” => last hour, “qdr:d” => last 24 hours, “qdr:m” => last month).
        safe (str) – Safe search.
        num (int) – Number of results per page.
        start (int) – First result to retrieve.
        stop (int) – Last result to retrieve. Use None to keep searching forever.
        pause (float) – Lapse to wait between HTTP requests. A lapse too long will make the search slow, but a lapse too short may cause Google to block your IP. Your mileage may vary!
        country (str) – Country or region to focus the search on. Similar to changing the TLD, but does not yield exactly the same results. Only Google knows why…
        extra_params (dict) – A dictionary of extra HTTP GET parameters, which must be URL encoded. For example if you don’t want Google to filter similar results you can set the extra_params to {‘filter’: ‘0’} which will append ‘&filter=0’ to every query.
        user_agent (str) – User agent for the HTTP requests. Use None for the default.
        verify_ssl (bool) – Verify the SSL certificate to prevent traffic interception attacks. Defaults to True.

    Return type:	

    generator of str
    Returns:	

    Generator (iterator) that yields found URLs. If the stop parameter is None the iterator will loop forever.

googlesearch.lucky(*args, **kwargs)[source]

    Shortcut to single-item search.

    Same arguments as the main search function, but the return value changes.
    Return type:	str
    Returns:	URL found by Google.

googlesearch.get_random_user_agent()[source]

    Get a random user agent string.
    Return type:	str
    Returns:	Random user agent string.

googlesearch.get_tbs(from_date, to_date)[source]

    Helper function to format the tbs parameter.
    Parameters:	

        from_date (datetime.date) – Python date object.
        to_date (datetime.date) – Python date object.

    Return type:	

    str
    Returns:	

    Dates encoded in tbs format.
    
    ### the above taken from [Mario Vilas](https://python-googlesearch.readthedocs.io/en/latest/)
