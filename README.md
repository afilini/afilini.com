# afilini.com

Source code of my personal website, hosted at <https://afilini.com>.

The website is built with [hugo](https://gohugo.io/), to run it locally you can use:

```
hugo serve
```

which will start listening on <http://localhost:1313>.

Note that in order to correctly pull the theme you should either clone `recursively` or initialize the submodules after you've cloned the repo.

## Making Changes

If you wanna make changes to this website there are a few things you can use to make your life easier:

### Hooks

You can run `./scripts/apply-git-hooks.sh` to install the git hooks shipped with this repo under `.githooks/`. They run a few checks before creating a commit, to ensure everything is ready to be published.

### Links

Since URLs on the internet are not really permanent, all the external links I add in my blog are gonna be archived with <https://archive.is>. To make the process a bit less tedious there's the `./scripts/fetch-url-archive.py` python
script which can be used to create all the required markdown stuff for a given link.

Make sure you install the dependencies from `./scripts/requirements.txt` before using the script.

Running it with `./scripts/fetch-url-archive.py <URL>` will assume you want to link to the URL as a note at the end of the page.

Running it with `./scripts/fetch-url-archive.py <URL> <TEXT>` will assume you want to make an inline link with the text "TEXT".

### Generating the Share Picture

To regenerate `./static/images/share.png` you can use the `./scripts/update-share-screenshot.py`. Again, this requires the dependencies from `./scripts/requirements.txt`, plus Firefox and Geckodriver installed.

The hugo server should also be running in background to allow the script to capture a screenshot of the page.

## License

The content of the website is licensed under [CC BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/).
