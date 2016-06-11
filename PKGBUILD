pkgname="mpis-unstable-git"
_pyname="mpis"
_gitname="Script-Post-instalacion"
pkgver="0.1a"
pkgrel="1"
pkgdesc="This script allows to configure the system, install some applications for a regular work day thinked in developers, gamers, musicians and more... Unstable branch from Git."
arch=('any')
url="https://kernelpanicblog.wordpress.com"
license=('gplv3')
makedepends=('python-setuptools')
source=("git+https://github.com/KernelPanicBlog/Script-Post-instalacion.git#branch=unstable")
md5sums=('SKIP')

package() {
  cd "${srcdir}/${_gitname}"
  python3 setup.py install --prefix=/usr --root="${pkgdir}"
  install -d -m755 "${pkgdir}/usr/lib/${_pyname}" "${pkgdir}/usr/share/licenses/${_pyname}"
  install -m644 LICENSE "${pkgdir}/usr/share/licenses/${_pyname}/LICENSE"
  install -m644 apps.config "${pkgdir}/usr/lib/${_pyname}/apps.config"
  install -m644 menus.config "${pkgdir}/usr/lib/${_pyname}/menus.config"
}
