import requests
import csv
import json


proxies={
    'http': '45.85.163.86:8000',
    'https': '45.85.163.86:8000',
}

cookies = {
    '__cpcPopShown': '1',
    '__cpc': 'YS9TWjB0Qkw2YnQxYWdXVVhNZlJCa00yN3kyODF2NmY2VkJMZURXVUdlWTVsMUZCR0F4QTB4Q0YrQXRXQ0MvZWtodm1WdUhDZ2NGZ25FbGl6STJQdUxSTWF4QlZGL2lFbng5b0ViZjB6VldjcHBpU0hCOSt3NlBtajRKZGUrMC9XRzFIMlpHeDgrSHFLbXVRcFFpR0dvM0ZqLzFXeElybndUQ2V0VHcvUFc5ek1iYUhBdERyVnlJUENvSlc3OXdxWVllRDVOS1FtV2JpOW9IazNxKzZxdk1BaElzYWNsVHUzRzg0c1dIN1FTOWVaUjRHVmk4OGlRK3JhT253WWNMWk1mR01YenRFNzF1c3NuR3BoSVdOTXVVYTkrMGh1ZkF6eHVsclkya3R2WkFyNDFsUmt3KzhBNUZvNEVPdFV4WE1sMVBOQjJSbXVMYWh2UGpUb2JnYVRTZm1mQjNtTFRaalZCSHorb1ByMElpaGR3TTRKSi9rY1d4UDg4WVhwYXJWZzhxZm1ld3U1aGhLam13eTVYMUdHZnJWUElsd0VyYVoxdmkzYTA3c1M3UT0=',
    'guest_id@twitter.com': 'v1%3A172896951875449330',
    'guest_id@x.com': 'v1%3A172896951875449330',
    'night_mode@x.com': '2',
    '__cpcStatSampleNum': '2',
    'd_prefs@x.com': 'MToxLGNvbnNlbnRfdmVyc2lvbjoyLHRleHRfdmVyc2lvbjoxMDAw',
    'guest_id_ads@x.com': 'v1%3A172896951875449330',
    'guest_id_marketing@x.com': 'v1%3A172896951875449330',
    'personalization_id@x.com': '"v1_h9gLd23xz5iR/aLcBcZMiQ=="',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    # 'Cookie': '__cpcPopShown=1; __cpc=YS9TWjB0Qkw2YnQxYWdXVVhNZlJCa00yN3kyODF2NmY2VkJMZURXVUdlWTVsMUZCR0F4QTB4Q0YrQXRXQ0MvZWtodm1WdUhDZ2NGZ25FbGl6STJQdUxSTWF4QlZGL2lFbng5b0ViZjB6VldjcHBpU0hCOSt3NlBtajRKZGUrMC9XRzFIMlpHeDgrSHFLbXVRcFFpR0dvM0ZqLzFXeElybndUQ2V0VHcvUFc5ek1iYUhBdERyVnlJUENvSlc3OXdxWVllRDVOS1FtV2JpOW9IazNxKzZxdk1BaElzYWNsVHUzRzg0c1dIN1FTOWVaUjRHVmk4OGlRK3JhT253WWNMWk1mR01YenRFNzF1c3NuR3BoSVdOTXVVYTkrMGh1ZkF6eHVsclkya3R2WkFyNDFsUmt3KzhBNUZvNEVPdFV4WE1sMVBOQjJSbXVMYWh2UGpUb2JnYVRTZm1mQjNtTFRaalZCSHorb1ByMElpaGR3TTRKSi9rY1d4UDg4WVhwYXJWZzhxZm1ld3U1aGhLam13eTVYMUdHZnJWUElsd0VyYVoxdmkzYTA3c1M3UT0=; guest_id@twitter.com=v1%3A172896951875449330; guest_id@x.com=v1%3A172896951875449330; night_mode@x.com=2; gt@x.com=1846058094607888602; __cpcStatSampleNum=2; d_prefs@x.com=MToxLGNvbnNlbnRfdmVyc2lvbjoyLHRleHRfdmVyc2lvbjoxMDAw; guest_id_ads@x.com=v1%3A172896951875449330; guest_id_marketing@x.com=v1%3A172896951875449330; personalization_id@x.com="v1_h9gLd23xz5iR/aLcBcZMiQ=="',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'content-type': 'application/json',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'x-client-transaction-id': 'DyamtTIiyTvLW9uaOUD4Ms6zQPbXSPPQ+z2jwfyuEhO62h3h7Poy+I+KEkwktJGhKNqYsQ1zutcLCs4bveQIZaA3GfjQDA',
    # 'x-guest-token': '1846122688865087594',
    'x-twitter-active-user': 'yes',
    'x-twitter-client-language': 'ru',
}

params = {
    'variables': '{"userId":"44196397","count":20,"includePromotedContent":true,"withQuickPromoteEligibilityTweetFields":true,"withVoice":true,"withV2Timeline":true}',
    'features': '{"rweb_tipjar_consumption_enabled":true,"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"communities_web_enable_tweet_community_results_fetch":true,"c9s_tweet_anatomy_moderator_badge_enabled":true,"articles_preview_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":true,"tweet_awards_web_tipping_enabled":false,"creator_subscriptions_quote_tweet_preview_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"rweb_video_timestamps_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_enhance_cards_enabled":false}',
    'fieldToggles': '{"withArticlePlainText":false}',
    '__cpo': 'aHR0cHM6Ly9hcGkueC5jb20',
}


def get_x_quest_token():
    url = "https://api.twitter.com/1.1/guest/activate.json"
    auth = {
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    }

    response = requests.post(url, headers=auth, proxies=proxies)
    data = json.loads(response.text)

    guest_token = data["guest_token"]
    headers['x-guest-token'] = guest_token


def get_response():
    response = requests.get(
        'https://twitter.com/i/api/graphql/Tg82Ez_kxVaJf7OPbUdbCg/UserTweets',
        params=params,
        cookies=cookies,
        headers=headers,
        proxies=proxies,
    )
    return response


def get_tweets(response):
    json_response = response.json()
    result = json_response.get("data", {}).get("user", {}).get("result", {})
    timeline = result.get("timeline_v2", {}).get("timeline", {}).get("instructions", {})
    entries = [x.get("entries") for x in timeline if x.get("type") == "TimelineAddEntries"]
    entries = entries[0] if entries else []
    _tweets = []

    for entry in entries:
        content = entry.get("content")
        item_result = content.get("itemContent", {}).get("tweet_results", {}).get("result", {})
        legacy = item_result.get("legacy").get("full_text")

        _tweets.append(legacy)

    return _tweets[:10]


def main():
    get_x_quest_token()
    response = get_response()
    _tweets = get_tweets(response)
    print(_tweets)


if __name__ == '__main__':
    main()
