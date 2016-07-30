pkgname="mpis-git"
_gitrepo="MPIS"
pkgver="0.2a"
pkgrel="1"
pkgdesc="This script allows to configure the system, install some applications for a regular work day thinked in developers, gamers, musicians and more..."
arch=("any")
url="https://kernelpanicblog.wordpress.com"
license=("GPLv3")
depends=("python3")
makedepends=("python-setuptools")
options=(!emptydirs)
source=("git+https://github.com/KernelPanicBlog/MPIS.git#branch=master")
md5sums=("SKIP")

package() {
  cd "$srcdir/$_gitrepo"
  python3 setup.py install --prefix=/usr --root="$pkgdir/" --optimize=1
}
