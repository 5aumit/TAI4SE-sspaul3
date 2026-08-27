package br.com.arturpessano.controller;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import br.com.arturpessano.model.Produto;
import br.com.arturpessano.service.ProdutoServico;

@RestController
@RequestMapping("/produto")
public class ProdutoControle {

	@Autowired
	private ProdutoServico produtoServico;

	@GetMapping
	public List<Produto> findAll() {
		return produtoServico.findAll();

	}

	@GetMapping("/{nome}")
	public Optional<Produto> findOne(@PathVariable int id) {
		return produtoServico.findOne(id);

	}

	@PostMapping
	public Map<String, String> insart(@RequestBody Produto produto) {
		Map<String, String> result = new HashMap<String, String>();

		produtoServico.insertOrUpdate(produto);

		return result;
	}

	@PutMapping
	public Map<String, String> edit(@RequestBody Produto produto) {
		Map<String, String> result = new HashMap<String, String>();
		produto = produtoServico.insertOrUpdate(produto);
		if (produto != null)
			result.put("result", "Produto editado com sucesso!!");
		else
			result.put("result", "Não foi possivel editar esse produto!!");
		return result;
	}

	@DeleteMapping("{id}")
	public void remove(@PathVariable int id) {

		produtoServico.remove(id);

	}

}
