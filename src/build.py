"""Is it heresy to use Python and make instead of JavaScript and npm for a build script?"""

import json
from glob import glob
from os import path


def apply_colors(template, colors):
    if isinstance(template, dict):
        return {key: apply_colors(value, colors)
                for key, value in template.items()}
    elif isinstance(template, list):
        return [apply_colors(value, colors) for value in template]
    elif isinstance(template, str) and template in colors:
        return colors[template]
    else:
        return template

def compile_variants():
    with open('package.json') as manifest:
        manifest = json.load(manifest)
    with open('src/dark-remix-template.json') as template:
        template = json.load(template)
    variants = glob("src/colors/*.json")
    for variant in variants:
        with open(variant) as colors:
            colors = json.load(colors)
            theme = apply_colors(template, colors)
            variant_name = path.basename(variant)[:-5]
            with open(f"build/themes/dark-remix-{variant_name}.json", 'w') as theme_file:
                json.dump(theme, theme_file, indent=4)
            manifest["contributes"]["themes"].append({
                "label": f"Dark+ Remix ({variant_name.replace('-', ' ').capitalize()})",
                "uiTheme": "vs-dark",
                "path": f"./themes/dark-remix-{variant_name}.json"
            })
    with open("build/package.json", 'w') as patched_manifest:
        json.dump(manifest, patched_manifest, indent=4)


if __name__ == "__main__":
    compile_variants()
