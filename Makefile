deploy: all publish

all: clean compile package

clean:
	rm -rf build

compile:
	mkdir build
	mkdir build/themes
	python3 ./src/build.py
	cp README.md CHANGELOG.md LICENSE.md icon.png screen-nord.png build/

package:
	cd build && vsce package

publish:
	cd build && vsce publish