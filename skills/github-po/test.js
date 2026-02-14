#!/usr/bin/env node

/**
 * Test de la skill github-po
 */

import {
  listRepos,
  createIssue,
  createPR,
} from "./index.js";

async function runTests() {
  console.log("🧪 Probando github-po...\n");

  // Test: listar repos (ejemplo con 'facebook')
  try {
    console.log("Test 1: Listando repos de 'facebook'...");
    const repos = await listRepos("facebook");
    console.log(`✅ Se encontraron ${repos.length} repos:`);
    repos.slice(0, 3).forEach(repo => {
      console.log(`  - ${repo.name}: ${repo.description}`);
    });
    console.log();
  } catch (error) {
    console.log(`❌ Test 1 falló: ${error.message}`);
    console.log();
  }

  // Nota: Los tests de crear issue y PR requieren token de GitHub
  console.log("Test 2 y 3: Crear issue y PR");
  console.log("Nota: Requiere autenticación (token de GitHub) para funcionar.");
  console.log();
}

runTests().catch(console.error);
