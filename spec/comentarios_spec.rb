# encoding: utf-8

require_relative '../comentarios.rb'

describe 'conta linhas de código' do

  describe "no estilo linha única" do
    it 'deve retornar zero com codigo vazio' do
      conta_linhas_de_codigo('').should == 0
    end

    it 'deve retornar zero com linhas em branco' do
      conta_linhas_de_codigo("\n\n\n\n").should == 0
    end

    it 'deve retornar 1 para 1 linha de código' do
      conta_linhas_de_codigo('public class teste() {}').should == 1
    end

    it 'deve retornar 0 para 1 linha de comentário' do
      conta_linhas_de_codigo('// este eh um comentario').should == 0
    end

    it 'deve retornar 1 para 1 linha de código e 1 linha comentada' do
      conta_linhas_de_codigo("// comentario\n int i;").should == 1
    end

    it 'deve retornar 1 para 1 linha de código e 1 linha comentada com espaco' do
      conta_linhas_de_codigo(" // comentario\n int i;").should == 1
    end

    it 'deve retornar 1 para 1 linha de código e 1 linha comentada com tabs' do
      conta_linhas_de_codigo("\t// comentario\n int i;").should == 1
    end

    it 'deve retornar 1 para 1 linha de código e 1 linha comentada com tabs/espaços' do
      conta_linhas_de_codigo("\t \t// comentario\n int i;").should == 1
    end

    it 'deve retornar 1 para 1 linha de código que comeca com apenas uma barra' do
      conta_linhas_de_codigo("/ comentario int i;").should == 1
    end
  end


  describe "comentários multi-linha" do
    it 'deve retornar 0 para 1 linha de comentário' do
      conta_linhas_de_codigo('/* este eh um comentario */').should == 0
    end

    it 'deve retornar 0 para varias linhas de comentário' do
      conta_linhas_de_codigo("/* este eh \n um comentario \n grande*/").should == 0
    end

  end
end