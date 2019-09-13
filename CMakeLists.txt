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

cmake_minimum_required ( VERSION 3.0 )
project( Alglib )

set( ${PROJECT_NAME}_VERSION_MAJOR 3 ) 		# Adjust here the version number manually
set( ${PROJECT_NAME}_VERSION_MINOR 15 ) 	# Adjust here the version number manually
set( ${PROJECT_NAME}_VERSION_PATCH 0 ) 		# Adjust here the version number manually
set( ${PROJECT_NAME}_DATE "Feb 21 2019" )

# generate the version info header file
configure_file (
	"${PROJECT_SOURCE_DIR}/source/cpp/src/version.template"
	"${PROJECT_SOURCE_DIR}/source/cpp/src/version.h"
)

set( SOURCE
	source/cpp/src/alglibinternal.cpp
	source/cpp/src/alglibmisc.cpp
	source/cpp/src/ap.cpp
	source/cpp/src/dataanalysis.cpp
	source/cpp/src/diffequations.cpp
	source/cpp/src/fasttransforms.cpp
	source/cpp/src/integration.cpp
	source/cpp/src/interpolation.cpp
	source/cpp/src/linalg.cpp
	source/cpp/src/optimization.cpp
	source/cpp/src/solvers.cpp
	source/cpp/src/specialfunctions.cpp
	source/cpp/src/statistics.cpp
)

add_library( alglib STATIC ${SOURCE} )

# enable SSE-optimizations for the Alglib-library on the supported platforms
if ( ${CMAKE_SYSTEM_PROCESSOR} MATCHES "(x86)|(X86)|(amd64)|(AMD64)" )
	target_compile_definitions( alglib PRIVATE
		AE_CPU=AE_INTEL
	)
endif()

target_compile_definitions( alglib PRIVATE
    -D_UNICODE -DUNICODE
)
