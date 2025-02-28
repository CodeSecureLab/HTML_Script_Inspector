# HTML Script Inspector

HTML Script Inspector is a tool that parses HTML files for script imports using regex patterns. It is currently in development and aims to provide comprehensive support for identifying and managing module imports in HTML files.

## Features

- Parses HTML files for script imports using regex patterns.
- Supports common CDNs and local script patterns.
- Outputs module information including path, module name, version, and line number.

## Usage

To run the tool, use the following command(until release):

```sh
python .\html_script_inspector\inspector_cli.py --path testing_dir
```

## Development

### Current Work

- Adding OSS Index support.
- Publish 1.0 as package

### Future Plans

- Add support for using an Open API key to parse for modules by using a flag.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License.