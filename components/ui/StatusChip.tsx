import styles from "./StatusChip.module.css";

type Status = "granted" | "locked" | "active" | "warning" | "error" | "muted" | "pending" | "info";

const labels: Record<Status, string> = {
  granted: "Access granted",
  locked: "Locked",
  active: "Active",
  warning: "Warning",
  error: "Error",
  muted: "Info",
  pending: "Pending",
  info: "Info",
};

export function StatusChip({
  status,
  children,
}: {
  status: Status;
  children?: string;
}) {
  return (
    <span className={`${styles.chip} ${styles[status]}`}>
      {children || labels[status]}
    </span>
  );
}
