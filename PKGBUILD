pkgname="mpis-unstable-git"
_pyname="mpis"
_gitrepo="Script-Post-instalacion"
pkgver="0.2a"
pkgrel="1"
pkgdesc="This script allows to configure the system, install some applications for a regular work day thinked in developers, gamers, musicians and more... Unstable branch from Git."
arch=('any')
url="https://kernelpanicblog.wordpress.com"
license=('gplv3')
makedepends=('python-setuptools')
source=("git+https://github.com/KernelPanicBlog/Script-Post-instalacion.git#branch=unstable")
md5sums=('SKIP')

package() {
  cd "${srcdir}/${_gitrepo}"
  python3 setup.py install --prefix=/usr --root="${pkgdir}"
}
