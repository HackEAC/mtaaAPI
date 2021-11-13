# Mtaa API

[Mtaa API](https://mtaa-api.herokuapp.com) is a simple REST(And later GraphQL) API for accessing Tanzania locations.

Mtaa API is powered by [mtaa](https://github.com/Kalebu/mtaa).

## Why?

Most of the time when coding, we found ourselves in need of some location data, especially for our country, [Tanzania](https://en.wikipedia.org/wiki/Tanzania).

We didn't like the idea of scraping some public sites because we had the feeling that we was spending more time understanding the site and cleaning the data than focusing on my task.

But we liked the idea of a public API for developers. So I decided to code a little Flask server inspired by our [tanzania-locations-db](https://github.com/HackEAC/tanzania-locations-db), [mtaa](https://github.com/Kalebu/mtaa) and here is Mtaa API.

You can find it running here and are free to use it in your developments: [https://mtaa-api.herokuapp.com/api](https://mtaa-api.herokuapp.com/api).

I hope you will find it useful.

## Features

* No registration
* Zero-config
* Basic API
* Cross-domain ([CORS](http://en.wikipedia.org/wiki/Cross-origin_resource_sharing))
* Supports GET and POST(GraphQL) verbs
* Compatible with React, Angular, Vue, Ember, ...
<!-- * HTTP or HTTPS -->
<!-- * "Has many" relationships -->
<!-- * Filters and nested resources -->

## Guide

For examples and more, documentation  you can visit https://mtaa-api.herokuapp.com/docs