package util;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class SettingsDB {
	
	//Datos de conexión a BD
	
	public static String databaseName = "craw";
	private static String ip = "127.0.0.1";
	private static String user = "root";
	private static String pwd = "root";
	private static String url = "jdbc:mysql://localhost/craw?useUnicode=true&useJDBCCompliantTimezoneShift=true&useLegacyDatetimeCode=false&serverTimezone=UTC";
	//private static String driver = "org.gjt.mm.mysql.Driver\r\n";
	private static String driver = "com.mysql.jdbc.Driver";
	private static String encode = "utf-8";

	public static Connection getConnection() {
		Connection connection = null;
		try {
			Class.forName(driver);
			connection = DriverManager.getConnection(url, user, pwd);
		} catch (Exception e) {
			e.printStackTrace();
		}
		return connection;
	}

	public static Statement createStmt(Connection conn) {
		Statement stmt = null;
		try {
			stmt = conn.createStatement();
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return stmt;
	}

	public static PreparedStatement createPreStmt(Connection conn, String sql) {
		PreparedStatement pstm = null;
		try {
			pstm = conn.prepareStatement(sql);
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return pstm;
	}

	public static ResultSet query(String sql, Statement stmt) {
		ResultSet rs = null;
		try {
			rs = stmt.executeQuery(sql);

		} catch (SQLException e) {
			e.printStackTrace();
		}
		return rs;
	}

	public static int update(String sql, Statement stmt) {
		int ret = 0;
		try {
			ret = stmt.executeUpdate(sql);
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return ret;
	}
	
	public static String queryExecute() {
		String script = " insert into diamundialcontraelcancerdemama (alias, nombre, twet, localizacion, fecha_registro)"
		        + " values (?, ?, ?, ?, ?)";
		
		return script;
	}

	public static void close(Connection conn, Statement stmt, PreparedStatement pstm, ResultSet rs) {
		close(rs);
		close(pstm);
		close(stmt);
		close(conn);
	}

	private static void close(Connection conn) {
		if (conn != null) {
			try {
				conn.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
			conn = null;
		}
	}

	private static void close(Statement stmt) {
		if (stmt != null) {
			try {
				stmt.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
			stmt = null;
		}
	}

	private static void close(PreparedStatement pstm) {
		if (pstm != null) {
			try {
				pstm.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
			pstm = null;
		}
	}

	private static void close(ResultSet rs) {
		if (rs != null) {
			try {
				rs.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
			rs = null;
		}
	}
}
