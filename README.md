# URLs to eBook 



This project offers a Python script and GitHub Actions workflow designed to automate the conversion of content from specified URLs into an eBook format. The Python script extracts the content from each URL, converts it into Markdown format, and then compiles the content into an eBook. The GitHub Actions workflow facilitates the execution of this script, allowing for automated eBook generation, optional email delivery, and repository commit actions.

## Features

- **Content Extraction:** Utilizes the [`mercury-parser`](https://github.com/postlight/mercury-parser) to fetch and parse content from provided URLs.
- **Markdown Conversion:** Converts the parsed content into Markdown format using [`markdownify`](https://github.com/matthewwithanm/python-markdownify).
- **eBook Compilation:** Compiles the Markdown files into an eBook using [`pandoc`](https://pandoc.org/) and converts it to `.mobi` format with [`calibre`](https://calibre-ebook.com/).
- **Custom Workflow Triggers:** Triggered manually via GitHub's `workflow_dispatch` event, allowing dynamic input of URLs.
- **Email Delivery:** Optionally sends the generated eBook to a specified email address (e.g. kindle one)
- **Version Control Integration:** optionally commits the generated eBook to the repository based on user input.


## Usage

To use this GitHub Action in your project, follow these steps:

1. **Create a repository based on this template** into your GitHub account or organization.
2. If needed, customize the `.github/workflows/news.yml` workflow.
3. **Trigger the workflow** manually via GitHub's UI passing

## Contributing

Contributions to improve this project are welcome. Please consider submitting issues for bugs or suggestions and pull requests for code contributions.

## License

This project is open source and available under [MIT License](LICENSE).