/*
 * Copyright 2015-2018 the original author or authors.
 *
 * All rights reserved. This program and the accompanying materials are
 * made available under the terms of the Eclipse Public License v2.0 which
 * accompanies this distribution and is available at
 *
 * http://www.eclipse.org/legal/epl-v20.html
 */

package com.example.project;

public class Main {

	public boolean main() {
		return true;
	}

	public boolean isCountLine(String str) {
		str = str.trim();

		return !isSlashComment(str) &&
				!isBlankLine(str) &&
				!checkBlock(str);
	}

	public boolean isSlashComment(String str) {
		return str.startsWith("//");
	}

	public boolean isBlankLine(String str) {
		return str.length() == 0;
	}

	public boolean checkBlock(String str){
		return (str.startsWith("/*") &&
				str.endsWith("*/"));
	}

}
