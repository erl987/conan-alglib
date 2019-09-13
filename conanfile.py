# conan-alglib - Conan recipe for the Alglib-library Free Edition
# Copyright(C) 2019 Ralf Rettig (info@personalfme.de)
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.If not, see <http://www.gnu.org/licenses/>

from conans import ConanFile, CMake, tools
import os


class AlglibConan(ConanFile):
    name = "alglib"
    version = "3.15.0"
    license = "GPL license version 2 or later"
    author = "Ralf Rettig <info@personalfme.de>"
    url = "https://github.com/erl987/conan-alglib.git"
    homepage = "http://www.alglib.net"
    description = "Cross-platform numerical analysis and data processing library"
    topics = ("numerics", "scientific computing", "data analysis", "optimization", "solvers", "linear algebra",
              "fitting", "interpolation", "fft")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports = "CMakeLists.txt", "source/cpp/src/version.template"

    def source(self):
        file_name = "{}-{}.cpp.gpl.zip".format(self.name, self.version)
        path = "{}/translator/re/{}".format(self.homepage, file_name)
        tools.download(path, file_name)
        tools.unzip(file_name, destination="source")
        os.remove(file_name)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("gpl2.txt", dst="licenses", src="source/cpp")
        self.copy("gpl3.txt", dst="licenses", src="source/cpp")
        self.copy("*.h", dst="include", src="source/cpp/src")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = [self.name]

