pkgname=yttext
pkgver=1.0.0
pkgrel=1
pkgdesc="A lightweight CLI tool for fetching and saving YouTube video transcripts."
arch=('any')
url="https://github.com/Asaduddeenamr2006/yt-transcript-tool"
license=('MIT')

depends=(
    'python'
    'python-youtube-transcript-api'
)

makedepends=(
    'python-build'
    'python-installer'
    'python-setuptools'
)

source=(
    "https://codeload.github.com/Asaduddeenamr2006/yt-transcript-tool/tar.gz/refs/tags/v${pkgver}"
)

sha256sums=('SKIP')

build() {
    cd "$srcdir/yt-transcript-tool-$pkgver"
    python -m build --wheel --no-isolation
}

package() {
    cd "$srcdir/yt-transcript-tool-$pkgver"

    python -m installer \
        --destdir="$pkgdir" \
        dist/*.whl
}
