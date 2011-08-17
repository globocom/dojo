# encoding: utf-8

def conta_linhas_de_codigo(codigo)
  codigo.gsub!(%r{//.*$}, '').gsub!(/\/\*.*\*\//m, '')
  codigo.lines.select { |line| not line.strip.empty? }.count
end
