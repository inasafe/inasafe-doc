# This script tests files for various spelling and grammar issues

require 'fileutils'
require 'open-uri'

dirs = [ "./beginner/osm",
         "./beginner/qgis-inasafe",
         "./intermediate/osm",
         "./intermediate/qgis-inasafe",
         "./socialisation"
        ]

searches = [ "gray",
             "right click",
             "left click",
             "double click",
             "practice",
             "license",
             "color",
             "ize",
             "izing",
             "ization",
             "yze",
             "yzing",
             "southeast",
             "southwest",
             "northeast",
             "northwest",
             "population density",
             "up to date",
             "chapter",
             "modeling",
             "modeled",
             "occuring",
             "tool bar",
             "step by step",
             "hands on",
             "meter",
             "inquiry",
             "dropdown"
           ]

searches2 = ["center"]

searches3 = [".  "]



dirs.each do |dir|
  Dir.foreach(dir) do |f|
    next if f == '.' or f == '..'
    puts f
    
    linecount = 1
    File.foreach("#{dir}/#{f}") do |line|
      searches.each do |search_term|
        if line.include?(search_term)
          puts "#{linecount}: (#{search_term}) #{line}"
        end
      end
      linecount += 1
    end
  puts "------------------------\n"
  end
  puts "++++++++++++++++++++++++++++++++++++++++++++++++++\n\n\n"
end