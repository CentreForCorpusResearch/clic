<?xml version="1.0"?>

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

	
	<xsl:variable name="upper">ABCDEFGHIJKLMNOPQRSTUVWXYZ</xsl:variable>
	<xsl:variable name="lower">abcedfghijklmnopqrstuvwxyz</xsl:variable>
	


	<xsl:template match="/">
		<xsl:apply-templates select="//div"/>  
	</xsl:template>


	<xsl:template match="div[@type='chapter']">
		
		<div class="chapterDiv">
			<span><xsl:text>ID: </xsl:text><xsl:value-of select="@book"/><xsl:text>.</xsl:text><xsl:value-of select="@num"/></span>
			<h3>Chapter <xsl:value-of select="@num"/></h3>
			<xsl:apply-templates/>
		</div>
		
	</xsl:template>


	<xsl:template match="p">
		<p>		
			<xsl:choose>
				<xsl:when test="@highlight='true'"><xsl:attribute name="style">background-color: #c0c0ff</xsl:attribute></xsl:when>
			</xsl:choose>
			<xsl:apply-templates/>
		</p>
	</xsl:template>


	<xsl:template match="s">
		<xsl:choose>
			<xsl:when test="preceding-sibling::s"><xsl:text> </xsl:text></xsl:when>
		</xsl:choose>
		<span>	
			<xsl:choose>
				<xsl:when test="@highlight='true'"><xsl:attribute name="style">background-color: #c0c0ff</xsl:attribute></xsl:when>
			</xsl:choose>	
			<!-- 		
			<span>(<xsl:value-of select="@num"/>) </span>
			 -->
			<xsl:apply-templates select="toks"/>
		</span>
	</xsl:template>


	<xsl:template match="w">
		<span>
			<xsl:choose>
				<xsl:when test="@inv='node'">
					<xsl:attribute name="style">color: green; text-decoration: underline; font-weight: bold</xsl:attribute>
				</xsl:when>
				<xsl:when test="@inv='other'">
					<xsl:attribute name="style">color: blue; font-weight: bold</xsl:attribute>
				</xsl:when>	
			</xsl:choose>
			<xsl:attribute name="onclick">
				<xsl:text>getCFP('</xsl:text><xsl:value-of select="./text()"/><xsl:text>')</xsl:text>
			</xsl:attribute>
			<xsl:apply-templates/>
		</span>
		
	</xsl:template>


</xsl:stylesheet>
